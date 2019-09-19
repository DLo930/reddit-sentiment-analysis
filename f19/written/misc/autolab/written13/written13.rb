require "AssessmentBase.rb"

module Written13
  include AssessmentBase

  def assessmentInitialize(course)
    super("written13",course)
    @problems = []
  end

end
