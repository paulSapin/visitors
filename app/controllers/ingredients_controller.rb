class IngredientsController < ApplicationController
  before_action :set_ingredient, only: [:show, :edit, :update, :destroy]
  before_filter :admin_user, only: [:destroy]

  # GET /ingredients
  # GET /ingredients.json
  def index
    @ingredients = Ingredient.all

    @ingredients_primarios_activos = Ingredient.where(:material_type => "Materia Prima", :active_or_excipient =>"A")
    @ingredients_primarios_excipientes = Ingredient.where(:material_type => "Materia Prima", :active_or_excipient =>"X")
    @ingredients_empaque_primario = Ingredient.where(:material_type => "Material Empaque 1o")
    @ingredients_empaque_secundario = Ingredient.where(:material_type => "Material Empaque 2o")


    respond_to do |format|
      format.html # index.html.erb
      format.json { render json: @ingredients }
    end
  end

  # GET /ingredients/1
  # GET /ingredients/1.json
  def show
  end

  # GET /ingredients/new
  def new
    @ingredient = Ingredient.new
  end

  # GET /ingredients/1/edit
  def edit
  end

  # POST /ingredients
  # POST /ingredients.json
  def create
    @ingredient = Ingredient.new(ingredient_params)
    @ingredient.created_by     = current_user.id
    @ingredient.updated_by     = current_user.id

    respond_to do |format|
      if @ingredient.save
        format.html { redirect_to @ingredient, notice: 'El material se creó exitosamente.' }
        format.json { render :show, status: :created, location: @ingredient }
      else
        format.html { render :new }
        format.json { render json: @ingredient.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /ingredients/1
  # PATCH/PUT /ingredients/1.json
  def update
    @ingredient.updated_by     = current_user.id
    
    respond_to do |format|
      if @ingredient.update(ingredient_params)
        format.html { redirect_to @ingredient, notice: 'El material se editó exitosamente.' }
        format.json { render :show, status: :ok, location: @ingredient }
      else
        format.html { render :edit }
        format.json { render json: @ingredient.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /ingredients/1
  # DELETE /ingredients/1.json
  def destroy
    @ingredient.destroy
    respond_to do |format|
      format.html { redirect_to ingredients_url, notice: 'El material fue elimiado.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_ingredient
      @ingredient = Ingredient.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def ingredient_params
      params.require(:ingredient).permit(:name, :unit, :stock_max, :stock_min_threshold, :stock, :external_id, :material_type, :active_or_excipient, :description, :created_by, :updated_by)
    end
end
