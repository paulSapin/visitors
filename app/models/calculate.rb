class Calculate < ActiveRecord::Base
	belongs_to :product
	belongs_to :user

	#Validate Presence
	validates :qty,     						:presence => true

	#Validates Positive Integer
	validates :qty, :numericality => { :greater_than => 0 }
	validates :qty, numericality: { only_integer: true }


end
