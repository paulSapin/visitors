class CreateProducts < ActiveRecord::Migration
  def change
    create_table :products do |t|
      t.string :name
      t.text :description
      t.string :package
      t.integer :average_weigth, default: 0
      t.string :unit
      t.integer :stock
      t.integer :number_of_blisters_per_box
      t.integer :number_of_units_per_blister
      t.integer :max_units_to_produce
      t.string :production_limited_by
      t.string :shape
      t.integer :created_by
      t.integer :updated_by

      t.timestamps
    end
  end
end
