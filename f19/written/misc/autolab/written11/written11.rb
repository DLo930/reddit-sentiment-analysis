require "AssessmentBase.rb"

module Written11
  include AssessmentBase

  def assessmentInitialize(course)
    super("written11",course)
    @problems = []
  end

end
