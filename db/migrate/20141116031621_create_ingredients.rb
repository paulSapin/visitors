class CreateIngredients < ActiveRecord::Migration
  def change
    create_table :ingredients do |t|
      t.string :name
      t.string :unit
      t.integer :stock_max
      t.integer :stock_min_threshold
      t.integer :stock, default: 0
      t.string :external_id
      t.string :material_type
      t.string :active_or_excipient
      t.text :description
      t.integer :created_by
      t.integer :updated_by

      t.timestamps
    end
  end
end
