require "AssessmentBase.rb"

module Lab10
  include AssessmentBase

  def assessmentInitialize(course)
    super("lab10",course)
    @problems = []
  end

end
