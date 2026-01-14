class Ingredient < ActiveRecord::Base

	has_many :components
	belongs_to :user

	#Validate Presence
	validates 	:name, :unit, :stock, :external_id, :material_type,     						
				:presence => true

	#Validates Positive 
	validates :stock, :numericality => { :greater_than_or_equal_to => 0 }

	#Validates Only Integer
	validates :stock, numericality: { only_integer: true }

	#Validates Uniqueness of External ID
	validates :external_id, uniqueness: { case_sensitive: false }

end
