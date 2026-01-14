class CreateComponents < ActiveRecord::Migration
  def change
    create_table :components do |t|
      t.integer :product_id
      t.integer :ingredient_id
      t.decimal :qty, :precision => 6, :scale => 2
      t.integer :created_by
      t.integer :updated_by

      t.timestamps
    end
  end
end
