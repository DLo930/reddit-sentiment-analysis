require "AssessmentBase.rb"

module Written01
  include AssessmentBase

  def assessmentInitialize(course)
    super("written01",course)
    @problems = []
  end

end
