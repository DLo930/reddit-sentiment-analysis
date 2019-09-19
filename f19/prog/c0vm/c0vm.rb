require "AssessmentBase.rb"
require "modules/Autograde.rb"


module C0vm
        include AssessmentBase
        include Autograde


        def assessmentInitialize(course)
                super("c0vm",course)
                @problems = []
        end

end

