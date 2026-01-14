require 'test_helper'

class IngredientsControllerTest < ActionController::TestCase
  setup do
    @ingredient = ingredients(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:ingredients)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create ingredient" do
    assert_difference('Ingredient.count') do
      post :create, ingredient: { active_or_excipient: @ingredient.active_or_excipient, created_by: @ingredient.created_by, description: @ingredient.description, external_id: @ingredient.external_id, material_type: @ingredient.material_type, name: @ingredient.name, stock: @ingredient.stock, stock_max: @ingredient.stock_max, stock_min_threshold: @ingredient.stock_min_threshold, unit: @ingredient.unit, updated_by: @ingredient.updated_by }
    end

    assert_redirected_to ingredient_path(assigns(:ingredient))
  end

  test "should show ingredient" do
    get :show, id: @ingredient
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @ingredient
    assert_response :success
  end

  test "should update ingredient" do
    patch :update, id: @ingredient, ingredient: { active_or_excipient: @ingredient.active_or_excipient, created_by: @ingredient.created_by, description: @ingredient.description, external_id: @ingredient.external_id, material_type: @ingredient.material_type, name: @ingredient.name, stock: @ingredient.stock, stock_max: @ingredient.stock_max, stock_min_threshold: @ingredient.stock_min_threshold, unit: @ingredient.unit, updated_by: @ingredient.updated_by }
    assert_redirected_to ingredient_path(assigns(:ingredient))
  end

  test "should destroy ingredient" do
    assert_difference('Ingredient.count', -1) do
      delete :destroy, id: @ingredient
    end

    assert_redirected_to ingredients_path
  end
end
