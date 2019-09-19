require "AssessmentBase.rb"

module Rec04
  include AssessmentBase

  def assessmentInitialize(course)
    super("rec04",course)
    @problems = []
  end

end
