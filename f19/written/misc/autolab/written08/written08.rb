require "AssessmentBase.rb"

module Written08
  include AssessmentBase

  def assessmentInitialize(course)
    super("written08",course)
    @problems = []
  end

end
