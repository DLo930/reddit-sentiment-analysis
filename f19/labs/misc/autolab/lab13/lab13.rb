require "AssessmentBase.rb"

module Lab13
  include AssessmentBase

  def assessmentInitialize(course)
    super("lab13",course)
    @problems = []
  end

end
