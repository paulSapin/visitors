class User < ActiveRecord::Base
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :trackable, :validatable



  has_many :calculates 
  has_many :components 
  has_many :ingredients 
  has_many :products, foreign_key: "created_by"

end
