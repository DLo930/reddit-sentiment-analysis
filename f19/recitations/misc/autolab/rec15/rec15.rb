require "AssessmentBase.rb"

module Rec15
  include AssessmentBase

  def assessmentInitialize(course)
    super("rec15",course)
    @problems = []
  end

end
