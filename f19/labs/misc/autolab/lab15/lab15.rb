require "AssessmentBase.rb"

module Lab15
  include AssessmentBase

  def assessmentInitialize(course)
    super("lab15",course)
    @problems = []
  end

end
