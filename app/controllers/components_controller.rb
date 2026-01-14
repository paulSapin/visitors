class ComponentsController < ApplicationController
  before_action :set_component, only: [:show, :edit, :update, :destroy]

  # GET /components
  # GET /components.json
  def index
    @components = Component.all
  end

  # GET /components/1
  # GET /components/1.json
  def show
  end

  # GET /components/new
  def new
    @component = Component.new

    @component.product_id = params[:id]
  end

  # GET /components/1/edit
  def edit
  end

  # POST /components
  # POST /components.json
  def create
    @component = Component.new(component_params)
    @component.created_by     = current_user.id
    @component.updated_by     = current_user.id


    respond_to do |format|
      if @component.save
        format.html { redirect_to product_path(@component.product_id), notice: 'El componente se agregó exitosamente.' }
        format.json { render :show, status: :created, location: @component }
      else
        format.html { render :new }
        format.json { render json: @component.errors, status: :unprocessable_entity }
      end
    end

    @product = Product.find(@component.product_id)
    @product.average_weigth = Component.where(:product_id => @component.product_id).joins(:ingredient).where(ingredients: {material_type:'Materia Prima'}).sum(:qty)
    @product.save

  end

  # PATCH/PUT /components/1
  # PATCH/PUT /components/1.json
  def update
    @component                = Component.find(params[:id])
    @component.updated_by     = current_user.id
    @product                  = Product.find(@component.product_id)

    respond_to do |format|
      if @component.update(component_params)
        format.html { redirect_to @product, notice: 'El component se editó exitosamente.' }
        format.json { render :show, status: :ok, location: @component }

        @product.average_weigth = Component.where(:product_id => @component.product_id).joins(:ingredient).where(ingredients: {material_type:'Materia Prima'}).sum(:qty)
        @product.save

      else
        format.html { render :edit }
        format.json { render json: @component.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /components/1
  # DELETE /components/1.json
  def destroy
    @product = Product.find(@component.product_id)
    @component.destroy

    @product.average_weigth = Component.where(:product_id => @component.product_id).joins(:ingredient).where(ingredients: {material_type:'Materia Prima'}).sum(:qty)
    @product.save

    respond_to do |format|
      format.html { redirect_to @product, notice: 'El componente fue eliminado.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_component
      @component = Component.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def component_params
      params.require(:component).permit(:product_id, :ingredient_id, :qty, :created_by, :updated_by)
    end
end
