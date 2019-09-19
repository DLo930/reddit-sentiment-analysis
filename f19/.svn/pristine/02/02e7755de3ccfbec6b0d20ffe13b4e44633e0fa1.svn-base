require "AssessmentBase.rb"
require "modules/Autograde.rb"
require("modules/Scoreboard.rb")

module Editorlab
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
    super("editorlab",course)
    @problems = [{'name'=>'gapbuf',
                   'description'=>'Gap buffers',
                   'max_score'=>10},
                 {'name'=>'dll',
                   'description'=>'Doubly-linked lists',
                   'max_score'=>5},
                 {'name'=>'tbuf',
                   'description'=>'Text buffers',
                   'max_score'=>10},
                 {'name'=>'style',
                   'description'=>"Style points assigned by instructor",
                   'max_score'=>5}]
  end

  def max_score
    30.0
  end

  def autogradingTimeout
    450
  end

  def autogradingImage
    "rhel122.img" # Required for coin and cc0 
  end

  ############################################
  # Autograder (should match new default impl)
  ############################################
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

  ###################################################
  ## Parse autoresult (should match new default impl)
  ###################################################
  def parseAutoresult(autoresult,isOfficial)
    begin
      parsed = ActiveSupport::JSON.decode(autoresult)
      if !parsed then
        raise "Empty autoresult"
      end
      if !parsed['scores'] then
        raise "Missing 'scores' object in the autoresult"
      end
      return parsed['scores']
    rescue
      return {'gapbuf'=>0,
        'dll'=>0,
        'tbuf'=>0}
    end
  end

  #############
  ## Scoreboard
  #############
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
    entry = []
    entry << createScoreboardOne(scores["gapbuf"],10)
    entry << createScoreboardOne(scores["dll"],5)
    entry << createScoreboardOne(scores["tbuf"],10)
    return entry
  end

  def scoreboardHeader
    return "<h3>Editorlab: Submission information anonymized by nickname.</h3>
        <table class='prettyBorder'>
        <tr><th>Nickname</th><th>version</th><th>Time</th>
        <th>Gap Buffers</th>
        <th>Doubly-Linked Lists</th>
        <th>Text Buffers</th>
        </tr>"
  end    

end
