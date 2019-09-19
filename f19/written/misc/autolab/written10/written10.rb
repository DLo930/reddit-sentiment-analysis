require "AssessmentBase.rb"

module Written10
  include AssessmentBase

  def assessmentInitialize(course)
    super("written10",course)
    @problems = []
  end

end
