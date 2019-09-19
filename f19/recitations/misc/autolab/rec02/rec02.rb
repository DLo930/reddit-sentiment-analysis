require "AssessmentBase.rb"

module Rec02
  include AssessmentBase

  def assessmentInitialize(course)
    super("rec02",course)
    @problems = []
  end

end
