require "AssessmentBase.rb"

module Rec03
  include AssessmentBase

  def assessmentInitialize(course)
    super("rec03",course)
    @problems = []
  end

end
