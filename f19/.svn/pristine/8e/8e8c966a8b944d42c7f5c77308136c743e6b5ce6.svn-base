# Are these next three lines necessary?
require "AssessmentBase.rb"
require "modules/Autograde.rb"
require("modules/Scoreboard.rb")

module Imagelab
  include AssessmentBase
  include Autograde
  include Scoreboard
  
  ##################### 
  # General functions #
  #####################


  # assessmentInitialize - this function is used exactly once, when
  # the lab is first installed in a course. After that, any changes
  # to the problems are done on the web page.
  def assessmentInitialize(course)
    super("imagelab",course)
    @problem_names = ['imageutil',
                      'invert',
                      'reflect',
                      'mask',
                      'manipulate']
    @problems = [{'name'=>'imageutil',
                   'description'=>"Implementing imageutil library",
                   'max_score'=>5},
                 {'name'=>'invert',
                   'description'=>"Implementing image inversion",
                   'max_score'=>4},
                 {'name'=>'reflect',
                   'description'=>"Implementing image reflection",
                   'max_score'=>5},
                 {'name'=>'mask',
                   'description'=>"Implementing mask application",
                   'max_score'=>6},
                 {'name'=>'manipulate',
                   'description'=>"A manipulation of your choice",
                   'max_score'=>1},
                 {'name'=>'style',
                   'description'=>"Style points assigned by instructor",
                   'max_score'=>5},
                 {'name'=>'theory',
                   'description'=>"Theory homework score",
                   'max_score'=>25}
                ]
  end

  def raw_score(scores)
    raw_score = 0.0
    scores.each { |name,score|
      case name
      when "manipulate"
        # Should be able to simply type break, but this results in a lower score
        # than should be the case.
        raw_score += 0.0
#      when "style"
#        raw_score += 0.0
      when "output"
        raw_score += 0.0
      else
        raw_score += score.to_f()
      end
    }
    return raw_score
  end

  # max_score - Maximum score for a lab that will printed on the
  # gradebook columns (optional)
  def max_score
    50.0
  end
  
  #########################
  # Autograding functions #
  #########################

  # autogradingTimeout - Lab-specific timeout (optional)
  def autogradingTimeout
    180
  end
  
  # autogradingImage - Virtual machine image (required)
  def autogradingImage
    "rhel122.img" # Required for coin and cc0
  end

  # autogradeInputFiles - Specifies the input files that are needed
  # by the autograder (required)
  def autogradeInputFiles(assessmentDir)
    
    handinFile = File.join(assessmentDir,
                           @assessment.handin_directory,
                           @submission.filename)
    makeFile = File.join(assessmentDir,"autograde-Makefile")
    graderFile = File.join(assessmentDir, "autograde.tar")
    
    f_handin =InputFile.new(:localFile=>handinFile,
                            :destFile=>"handin.tar")
    f_make = InputFile.new(:localFile=>makeFile,
                           :destFile=>"Makefile")
    f_grader = InputFile.new(:localFile=>graderFile,
                             :destFile=>"autograde.tar")

    return [f_handin, f_make, f_grader]
  end

  def getMeMyAutoresult(autoresult)
    begin
      parsed = ActiveSupport::JSON.decode(autoresult)
      if !parsed then
        raise "Empty autoresult"
      end
      if !parsed["scores"] then
        raise "Missing 'scores' object in the autoresult"
      end
      return parsed
    rescue
      return {'scores'=>
               {'invert'=>0,
                'imageutil'=>0,
                'reflect'=>0,
                'mask'=>0},
              'output'=>'carnegie'}
    end
  end

  # parseAutoresult - Tells Autolab how to parse the autoresult from
  # the Autograder so it can enter the results in the gradebook
  # (required)
  def parseAutoresult(autoresult,isOfficial)
    autores = getMeMyAutoresult(autoresult)
    return autores['scores'] 
  end

  #################################
  # Optional scoreboard functions #
  #################################

  def createScoreboardOne(score,max) 
    if score == 0 
      return "<span style='color:#900'>none</span>"
    end
    if score == max
      return "<span style='color:#090'>full</span>"
    end
    return "<span style='color:#990'>some</span>"
  end

  def createScoreboardEntry(scores,autoresult)
    autores = getMeMyAutoresult(autoresult)

    entry = []
    entry << createScoreboardOne(scores["imageutil"],5)
    entry << createScoreboardOne(scores["invert"],4)
    entry << createScoreboardOne(scores["reflect"],5)
    entry << createScoreboardOne(scores["mask"],6)

    url = "http://www.contrib.andrew.cmu.edu/~rjsimmon/imagelab/"
    url = url+autores["output"]
    if autores["output"] == "carnegie"
      entry << "(none)"
    else
      entry << ("<a href='"+url+".png'><img src='"+url+"-thumb.png'/></a>")
    end
    return entry
  end

  # createScoreboardEntry - Specify how to create a row in the
  # scoreboard given an autoresult
  #def createScoreboardEntry(scores,autoresult)
  #	if not autoresult =~ /AUTORESULT_STRING=/ then 
  #		scores = [0, 0, 0, 0]
  #		return scores
  #	end
  #	autoscores = (autoresult.split("="))[1].split(":")
  #	perfindex = autoscores[1].to_f()
  #	thruput = autoscores[2].to_f()
  #	efficiency = autoscores[3].to_f()
  
  #	tmphash = {}
  #	tmphash["Autograded Score"] = perfindex
  #	score = raw_score(tmphash)
  
  #	scores = [score, perfindex, thruput, efficiency]
  #	return scores
  #end
  
  # scoreboardOrderSubmissions - Specify how to order scoreboard
  # entries
  #def scoreboardOrderSubmissions(a, b)
  #    a_score = a[:entry][0].to_f
  #    a_perfindex = a[:entry][1].to_f
  #    a_thruput = a[:entry][2].to_f
  #    b_score = b[:entry][0].to_f
  #    b_perfindex = b[:entry][1].to_f
  #    b_thruput = b[:entry][2].to_f
  
  #   if (b_score != a_score)
  #       b_score <=> a_score    # descending order by score
  #   elsif (a_perfindex != b_perfindex)
  #       b_perfindex <=> a_perfindex  # then descending by perfindex
  #   elsif (a_thruput != b_thruput)
  #       b_thruput <=> a_thruput  # then descending order by thruput
  #   else
  #       a[:time] <=> b[:time]  # then ascending order by submission time
  #   end
  #end

  def scoreboardHeader
    return "<h3>Imagelab: Submission information anonymized by nickname.</h3>
        <table class='prettyBorder'>
        <tr><th>Nickname</th><th>version</th><th>Time</th>
        <th>imageutil</th>
        <th>invert</th>
        <th>reflect</th>
        <th>mask</th>
        <th>manipulate</th></tr>"
  end    

  
  #### Example header from 15-213; perhaps we should customize our scoreboards
  #### in a similar way eventually.
  
  # scoreboardHeader - Specify the header for the scoreboard page
  #def scoreboardHeader()
  #"<h3>This page shows your most recent submission. As always, please do your first handin early to avoid handin surprises.</h3>
  #<table class=\'sortable prettyBorder\' >
  #<tr>
  #<th>Nickname</th>
  #<th>Version</th>
  #<th>Date</th>
  #<th>Score</th>
  #<th>PerfIndex</th>
  #<th>KOps</th>
  #<th>Util (%)</th>
  #</tr>"
  #end
  
  
end

