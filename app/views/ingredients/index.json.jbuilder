json.array!(@ingredients) do |ingredient|
  json.extract! ingredient, :id, :name, :unit, :stock_max, :stock_min_threshold, :stock, :external_id, :material_type, :active_or_excipient, :description, :created_by, :updated_by
  json.url ingredient_url(ingredient, format: :json)
end
