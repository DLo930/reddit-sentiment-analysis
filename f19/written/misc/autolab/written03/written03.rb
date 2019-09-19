require "AssessmentBase.rb"

module Written03
  include AssessmentBase

  def assessmentInitialize(course)
    super("written03",course)
    @problems = []
  end

end
