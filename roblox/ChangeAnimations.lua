-- LocalScript under Character

local runAnimationId = "rbxassetid://18618439306" -- replace these with your own animation ids
local jumpAnimationId = "rbxassetid://18618443642" -- replace these with your own animation ids

local runAnimation = Instance.new("Animation")
runAnimation.AnimationId = runAnimationId

local jumpAnimation = Instance.new("Animation")
jumpAnimation.AnimationId = jumpAnimationId

local assets = {
	runAnimation,
	jumpAnimation,
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
