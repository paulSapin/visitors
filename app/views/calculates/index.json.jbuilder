json.array!(@calculates) do |calculate|
  json.extract! calculate, :id, :product_id, :qty
  json.url calculate_url(calculate, format: :json)
end
