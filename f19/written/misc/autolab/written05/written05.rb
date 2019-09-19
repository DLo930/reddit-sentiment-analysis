require "AssessmentBase.rb"

module Written05
  include AssessmentBase

  def assessmentInitialize(course)
    super("written05",course)
    @problems = []
  end

end
