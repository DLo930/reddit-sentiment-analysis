require "AssessmentBase.rb"

module Lab12
  include AssessmentBase

  def assessmentInitialize(course)
    super("lab12",course)
    @problems = []
  end

end
