require "AssessmentBase.rb"

module Written00
  include AssessmentBase

  def assessmentInitialize(course)
    super("written00",course)
    @problems = []
  end

end
