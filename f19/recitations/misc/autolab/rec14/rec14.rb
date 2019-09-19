require "AssessmentBase.rb"

module Rec14
  include AssessmentBase

  def assessmentInitialize(course)
    super("rec14",course)
    @problems = []
  end

end
