require "AssessmentBase.rb"

module Written09
  include AssessmentBase

  def assessmentInitialize(course)
    super("written09",course)
    @problems = []
  end

end
