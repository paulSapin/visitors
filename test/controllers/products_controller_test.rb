require 'test_helper'

class ProductsControllerTest < ActionController::TestCase
  setup do
    @product = products(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:products)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create product" do
    assert_difference('Product.count') do
      post :create, product: { average_weigth: @product.average_weigth, created_by: @product.created_by, description: @product.description, max_units_to_produce: @product.max_units_to_produce, name: @product.name, number_of_blisters_per_box: @product.number_of_blisters_per_box, number_of_units_per_blister: @product.number_of_units_per_blister, package: @product.package, production_limited_by: @product.production_limited_by, shape: @product.shape, stock: @product.stock, unit: @product.unit, updated_by: @product.updated_by }
    end

    assert_redirected_to product_path(assigns(:product))
  end

  test "should show product" do
    get :show, id: @product
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @product
    assert_response :success
  end

  test "should update product" do
    patch :update, id: @product, product: { average_weigth: @product.average_weigth, created_by: @product.created_by, description: @product.description, max_units_to_produce: @product.max_units_to_produce, name: @product.name, number_of_blisters_per_box: @product.number_of_blisters_per_box, number_of_units_per_blister: @product.number_of_units_per_blister, package: @product.package, production_limited_by: @product.production_limited_by, shape: @product.shape, stock: @product.stock, unit: @product.unit, updated_by: @product.updated_by }
    assert_redirected_to product_path(assigns(:product))
  end

  test "should destroy product" do
    assert_difference('Product.count', -1) do
      delete :destroy, id: @product
    end

    assert_redirected_to products_path
  end
end
