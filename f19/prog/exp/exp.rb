require "AssessmentBase.rb"


module Exp
        include AssessmentBase


        def assessmentInitialize(course)
                super("exp",course)
                @problems = []
        end

end

