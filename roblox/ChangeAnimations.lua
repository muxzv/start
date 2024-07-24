-- LocalScript under Character

local runAnimation = "rbxassetid://18618439306" -- replace these with your own animation ids
local jumpAnimation = "rbxassetid://18618443642" -- replace these with your own animation ids

local character = script.Parent
local animateScript = character:WaitForChild("Animate")

animateScript.run.RunAnim.AnimationId = runAnimation
animateScript.walk.WalkAnim.AnimationId = runAnimation
animateScript.jump.JumpAnim.AnimationId = jumpAnimation
