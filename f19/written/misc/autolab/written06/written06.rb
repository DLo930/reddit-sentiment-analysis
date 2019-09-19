require "AssessmentBase.rb"

module Written06
  include AssessmentBase

  def assessmentInitialize(course)
    super("written06",course)
    @problems = []
  end

end
