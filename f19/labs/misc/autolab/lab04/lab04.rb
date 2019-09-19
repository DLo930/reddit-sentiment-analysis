require "AssessmentBase.rb"
require "modules/Autograde.rb"


module Lab04
  include AssessmentBase
  include Autograde


  def assessmentInitialize(course)
    super("lab04",course)
    @problems = []
  end

end
