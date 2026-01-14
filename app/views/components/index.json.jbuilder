json.array!(@components) do |component|
  json.extract! component, :id, :product_id, :ingredient_id, :qty, :created_by, :updated_by
  json.url component_url(component, format: :json)
end
