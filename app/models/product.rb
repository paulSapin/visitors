class Product < ActiveRecord::Base
	has_many :components
	has_many :calculates
	belongs_to :user, foreign_key: "created_by"

	#Validate Presence
	validates 	:name, :shape, :unit, :number_of_blisters_per_box, :number_of_units_per_blister,
				:presence => true

	#Validates Positive 
	validates 	:number_of_blisters_per_box,:number_of_units_per_blister, 
				:numericality => { :greater_than => 0 }

	#Validates Only Integer			
	validates 	:number_of_blisters_per_box, :number_of_units_per_blister, 
				numericality: { only_integer: true }
  
end
