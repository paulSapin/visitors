json.array!(@products) do |product|
  json.extract! product, :id, :name, :description, :package, :average_weigth, :unit, :stock, :number_of_blisters_per_box, :number_of_units_per_blister, :max_units_to_produce, :production_limited_by, :shape, :created_by, :updated_by
  json.url product_url(product, format: :json)
end
