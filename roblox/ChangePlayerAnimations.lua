-- LocalScript under Character

local runAnimationId = "rbxassetid://18826886136" -- replace these with your own animation ids
local jumpAnimationId = "rbxassetid://18834471405" -- replace these with your own animation ids
local toolslashAnimationId = "rbxassetid://18826882897" -- replace these with your own animation ids
local idleAnimationId = "rbxassetid://18834613915" -- replace these with your own animation ids

local NOHANDOUT_ID = 04484494845 -- не менять

local function DisableHandOut(character)
  local Animator = character.Animate
  local Animation = Instance.new("Animation")
  Animation.AnimationId = "http://www.roblox.com/asset/?id="..NOHANDOUT_ID

  local ToolNone = Animator:FindFirstChild("toolnone")
  if ToolNone then
    local NewTool = Instance.new("StringValue")
    NewTool.Name = "toolnone"
    Animation.Name = "ToolNoneAnim"
    Animation.Parent = NewTool
    ToolNone:Destroy()
    NewTool.Parent = Animator
  end
end

print("Alla test start")

local runAnimation = Instance.new("Animation")
runAnimation.AnimationId = runAnimationId

local jumpAnimation = Instance.new("Animation")
jumpAnimation.AnimationId = jumpAnimationId

local toolslashAnimation = Instance.new("Animation")
toolslashAnimation.AnimationId = toolslashAnimationId

local idleAnimation = Instance.new("Animation")
idleAnimation.AnimationId = idleAnimationId

local assets = {
  runAnimation,
  jumpAnimation,
  toolslashAnimation,
  idleAnimation,
}

local ContentProvider = game:GetService("ContentProvider")

-- This will be hit as each asset resolves
local callback = function(assetId, assetFetchStatus)
  print("PreloadAsync() resolved asset ID:", assetId)
  print("PreloadAsync() final AssetFetchStatus:", assetFetchStatus)
end

ContentProvider:PreloadAsync(assets, callback)

local character = script.Parent
local animateScript = character:WaitForChild("Animate")

animateScript.run.RunAnim.AnimationId = runAnimationId
animateScript.walk.WalkAnim.AnimationId = runAnimationId
animateScript.jump.JumpAnim.AnimationId = jumpAnimationId
animateScript.toolslash.ToolSlashAnim.AnimationId = toolslashAnimationId
animateScript.idle.Animation1.AnimationId = idleAnimationId
animateScript.idle.Animation2.AnimationId = idleAnimationId

DisableHandOut(character)

print("Alla test stop")
