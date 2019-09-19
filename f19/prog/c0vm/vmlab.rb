require "AssessmentBase.rb"
require "modules/Autograde.rb"
require("modules/Scoreboard.rb")

module Vmlab
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
    super("vmlab",course)
    @problems = [{'name'=>'compile',
                   'description'=>'initialization of variables',
                   'max_score'=>5},
                 {'name'=>'arithmetic',
                   'description'=>'arithmetic ops',
                   'max_score'=>25},
                 {'name'=>'locals',
                   'description'=>'local variables',
                   'max_score'=>15},
                 {'name'=>'conditionals',
                   'description'=>'loops and branches',
                   'max_score'=>25},
                 {'name'=>'functions',
                   'description'=>'function calls',
                   'max_score'=>20},
                 {'name'=>'memory',
                   'description'=>'memory implementation',
                   'max_score'=>10}]
  end

  def max_score
    100.0
  end

  def autogradingTimeout
    240
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
  def parseRawAutoresult(autoresult) 
    begin
      parsed = ActiveSupport::JSON.decode(autoresult)
      if !parsed then
        raise "Empty autoresult"
      end
      if !parsed['scores'] then
        raise "Missing 'scores' object in the autoresult"
      end
      return parsed
    rescue
      return {'scores'=>{'compile'=>0,
          'arithmetic'=>0,
          'locals'=>0,
          'conditionals'=>0,
          'functions'=>0,
          'memory'=>0
        },
        'bonus'=>0}
    end
  end

  def parseAutoresult(autoresult,isOfficial)
    parsed = parseRawAutoresult(autoresult)
    return parsed['scores']
  end

  #############
  ## Scoreboard
  #############
  def createScoreboardOne(score,max) 
    if score == max
      return "<span style='color:#090'>full</span>"
    end
    if score == 0 
      return "<span style='color:#900'>none</span>"
    end
    return "<span style='color:#990'>some</span>"
  end

  def createScoreboardEntry(scores,autoresult)
    result = parseRawAutoresult(autoresult)
    entry = []
    entry << createScoreboardOne(scores["arithmetic"],25)
    entry << createScoreboardOne(scores["locals"],15)
    entry << createScoreboardOne(scores["conditionals"],25)
    entry << createScoreboardOne(scores["functions"],20)
    entry << createScoreboardOne(scores["memory"],10)
    return entry
  end

  def scoreboardHeader
    return "<h3>Submission information is anonymized by nickname.</h3>
        <table class='prettyBorder'>
        <tr><th>Nickname</th><th>version</th><th>Handin time</th>
        <th>Arithmetic</th>
        <th>Locals</th>
        <th>Conditionals</th>
        <th>Functions</th>
        <th>Memory</th>
        </tr>"
  end

  # def scoreboardOrderSubmissions(a,b)
  #   aSum=0;bSum=0;
  #   for key in a[:problems].keys do
  #     aSum += a[:problems][key].to_i
  #   end
  #   for key in b[:problems].keys do
  #     bSum += b[:problems][key].to_i
  #   end
  #   if (aSum != bSum) then
  #     bSum <=> aSum
  #   else
  #     a[:entry][5].to_i <=> b[:entry][5].to_i
  #   end
  # end

end
