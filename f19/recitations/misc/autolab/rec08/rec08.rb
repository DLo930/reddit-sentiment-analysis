require "AssessmentBase.rb"

module Rec08
  include AssessmentBase

  def assessmentInitialize(course)
    super("rec08",course)
    @problems = []
  end

end
