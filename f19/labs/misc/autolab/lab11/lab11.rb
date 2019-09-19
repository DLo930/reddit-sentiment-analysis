require "AssessmentBase.rb"

module Lab11
  include AssessmentBase

  def assessmentInitialize(course)
    super("lab11",course)
    @problems = []
  end

end
