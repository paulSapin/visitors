class CreateCalculates < ActiveRecord::Migration
  def change
    create_table :calculates do |t|
      t.integer :product_id
      t.integer :qty
      t.integer :created_by
      t.integer :updated_by

      t.timestamps
    end
  end
end
