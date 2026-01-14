class Component < ActiveRecord::Base

  belongs_to :product
  belongs_to :ingredient
  belongs_to :user

	#Validates 
	validates_associated :product

	#Validate Presence
	validates :qty, :presence => true

	#Validates Positive 
	validates :qty, :numericality => { :greater_than => 0 }

end
