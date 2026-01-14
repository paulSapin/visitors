class ProductsController < ApplicationController
  before_action :set_product, only: [:show, :edit, :update, :destroy]
  before_filter :admin_user, only: [:destroy]

  # GET /products
  # GET /products.json
  def index
    @products = Product.all
  end

  # GET /products/1
  # GET /products/1.json
  def show
    @product = Product.find(params[:id])

    @components = Component.where(:product_id => @product.id)

    @components_materia_prima = @components.joins(:ingredient).where(ingredients: {material_type:'Materia Prima'})

    @components_material_empaque_primario = @components.joins(:ingredient).where(ingredients: {material_type:'Material Empaque 1o'})

    @components_material_empaque_secundario = @components.joins(:ingredient).where(ingredients: {material_type:'Material Empaque 2o'})
    
        #Calcular el maximo a producir----------   
    # 1. Para cada componente calcular el maximo que se puede producir de acuerdo al stock

    # 1.1 Inicializar a un numero muy grande el numero maximo de unidades a producir de dicho producto
    @product.max_units_to_produce = 1000000000

     @components.each do |component|

    # 2. Dividir el stock actual de cada componente entre lo que se necesita para producir una unidad (tableta o capsula) 
       @component_max_units_to_produce = (component.ingredient.stock / component.qty )/ ( @product.number_of_blisters_per_box * @product.number_of_units_per_blister)
       
    # 3. Comparar los componentes y ver cual tienen el numero mas pequeno, ese seria el numero maximo de unidades para el producto.
       if @component_max_units_to_produce < @product.max_units_to_produce
        @product.max_units_to_produce = @component_max_units_to_produce 
        @product.production_limited_by = component.ingredient.name      
       end

     end

     # 4. Si el numero maximo no cambiara con respecto al inicial. Dejarlo en "0".
     if @product.max_units_to_produce == 1000000000
       @product.max_units_to_produce = 0
     end

     @product.save

  end

  def calculate
    @product = Product.find(params[:id])
    
  end

  # GET /products/new
  def new
    @product = Product.new
  end

  # GET /products/1/edit
  def edit
  end

  # POST /products
  # POST /products.json
  def create
    @product = Product.new(product_params)
    @product.created_by     = current_user.id
    @product.updated_by     = current_user.id

    respond_to do |format|
      if @product.save
        format.html { redirect_to @product, notice: 'El producto se creó exitosamente.' }
        format.json { render :show, status: :created, location: @product }
      else
        format.html { render :new }
        format.json { render json: @product.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /products/1
  # PATCH/PUT /products/1.json
  def update
    @product.updated_by     = current_user.id
    
    respond_to do |format|
      if @product.update(product_params)
        format.html { redirect_to @product, notice: 'El producto se editó exitosamente.' }
        format.json { render :show, status: :ok, location: @product }
      else
        format.html { render :edit }
        format.json { render json: @product.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /products/1
  # DELETE /products/1.json
  def destroy
    @product.destroy
    respond_to do |format|
      format.html { redirect_to products_url, notice: 'El producto fue eliminado' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_product
      @product = Product.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def product_params
      params.require(:product).permit(:name, :description, :package, :average_weigth, :unit, :stock, :number_of_blisters_per_box, :number_of_units_per_blister, :max_units_to_produce, :production_limited_by, :shape, :created_by, :updated_by)
    end
end
