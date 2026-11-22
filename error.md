mhoodpc TDD% UE_ROOT="/Users/Shared/Epic Games/UE_5.8" \
bash TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/build_phase1_diagnostic.sh
================================================================
 Phase-1 Unreal build diagnostic — 2026-11-22T13:43:46Z
 Persistent log: /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/BUILD_DIAGNOSTIC_20261122T134346Z.log
 (If the terminal closes, this log file remains — cat it any time.)
================================================================
[diag] PASS  Engine found: UE_ROOT=/Users/Shared/Epic Games/UE_5.8
[diag] PASS  RunUAT.sh located: /Users/Shared/Epic Games/UE_5.8/Engine/Build/BatchFiles/RunUAT.sh
[diag] PASS  Build.sh located: /Users/Shared/Epic Games/UE_5.8/Engine/Build/BatchFiles/Mac/Build.sh
[diag] PASS  GenerateProjectFiles.sh located: /Users/Shared/Epic Games/UE_5.8/Engine/Build/BatchFiles/Mac/GenerateProjectFiles.sh
[diag] PASS  Project file present: /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/TDD_GAME.uproject
[diag] PASS  Module TDD_GAME declared in .uproject
[diag] PASS  Data header present: /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDOmegaValleyData.h
[diag] Generating project files (UBT must see Source/TDD_GAME)...
[diag] Exact command:
  /Users/Shared/Epic\ Games/UE_5.8/Engine/Build/BatchFiles/Mac/GenerateProjectFiles.sh  /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/TDD_GAME.uproject

Setting up Unreal Engine project files...

Setting up bundled DotNet SDK
/Users/Shared/Epic Games/UE_5.8/Engine/Binaries/ThirdParty/DotNet/10.0/mac-arm64
Log file: /Users/mhoodpc/Library/Application Support/Epic/UnrealBuildTool/Log_GPF.txt

Generating XCode project files:
Discovering modules, targets and source code for project...
Adding projects for all targets...
Adding projects for all targets took 0.21s
Adding projects for all game projects took 0.00s
Adding projects for all modules took 0.23s
DiscoverCSharpPrograms took 0.04s
/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/MetalShaderConverter.build.cs: warning: Referenced directory '/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/include/metal_irconverter_ext' does not exist.
/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/MetalShaderConverter.build.cs: warning: Referenced directory '/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/include/metal_irconverter_ext' does not exist.
Compiling with Mac SDK 27.2, minimum Target OS version 14.00
Adding additional Xcode project info took 1.72s
Compiling Rules Assemblies 100%
Creating Build Targets
Exception while creating build target for EventLoopUnitTests: Program targets are not currently supported from this engine distribution.
Exception while creating build target for DotNetPerforceLib: Program targets are not currently supported from this engine distribution.
Exception while creating build target for ChaosTestHarness: Program targets are not currently supported from this engine distribution.
/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/MetalShaderConverter.build.cs: warning: Referenced directory '/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/include/metal_irconverter_ext' does not exist.
/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/MetalShaderConverter.build.cs: warning: Referenced directory '/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/include/metal_irconverter_ext' does not exist.
Creating Build Targets 100%
Generating data for project indexing...
Creating Build Targets took 0.59s
Generating data for project indexing... 100%
Generating data for project indexing took 0.25s
Writing project files...
Writing xcode workspace /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/TDD_GAME (Mac).xcworkspace
Writing project files... 100%
Writing project files took 1.24s
Compiling Rules Assemblies

Generating QueryTargets data for editor...
Compiling Rules Assemblies 100%
Writing Query Target Info 100%
Generating QueryTargets data for editor took 0.01s

Result: Succeeded
Total execution time: 7.11 seconds
Trace written to file /Users/mhoodpc/Library/Application Support/Epic/UnrealBuildTool/Trace.uba with size 134.0kb
[diag] PASS  GenerateProjectFiles.sh exited 0
[diag] Building TDD_GAME (Development / Mac) via Build.sh (UnrealBuildTool)...
[diag] Exact build command:
  /Users/Shared/Epic\ Games/UE_5.8/Engine/Build/BatchFiles/Mac/Build.sh  TDD_GAME  Mac  Development  -project=/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/TDD_GAME.uproject  -WaitMutex  -architecture=arm64
@@TDD_BUILD_OUTPUT_BEGIN@@
Setting up bundled DotNet SDK
/Users/Shared/Epic Games/UE_5.8/Engine/Binaries/ThirdParty/DotNet/10.0/mac-arm64
Running dotnet Engine/Binaries/DotNET/UnrealBuildTool/UnrealBuildTool.dll TDD_GAME Mac Development -project=/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/TDD_GAME.uproject -WaitMutex -architecture=arm64
Log file: /Users/mhoodpc/Library/Application Support/Epic/UnrealBuildTool/Log.txt
Determining max actions to execute in parallel (10 physical cores, 10 logical cores)
  Executing up to 10 processes, one per physical core
UbaServer - Listening on 0.0.0.0:1345
Invalidating makefile for TDD_GAME (ispc deleted)
/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/MetalShaderConverter.build.cs: warning: Referenced directory '/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/include/metal_irconverter_ext' does not exist.
Compiling with Mac SDK 27.2, minimum Target OS version 14.00
Building TDD_GAME...
===== Toolchain Information =====
Using Clang compiler 21.1.6 (/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++)
  Apple clang version 21.0.0 (clang-2100.4.1.1) Target: arm64-apple-darwin27.2.0 Thread model: posix InstalledDir: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin
Using Clang archiver (/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/libtool)
  Apple clang version 21.0.0 (clang-2100.4.1.1) Target: arm64-apple-darwin27.2.0 Thread model: posix InstalledDir: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin
===== End Toolchain Information =====
Using Unreal Build Accelerator local executor to run 21 action(s)
  CPU 10 physical cores, 10 logical cores
  Memory 16 GB physical, 14.39 GB/16 GB committed
  UBA Storage capacity 40 GB
[1/21] Compile [Apple] SharedPCH.Engine.Project.ValApi.ValExpApi.Cpp20.h
[2/21] Compile [Apple] TDDMarketStall.cpp
[3/21] Compile [Apple] TDDNamedNPC.cpp
[4/21] Compile [Apple] TDDMarketSubsystem.cpp
[5/21] Compile [Apple] TDDForbiddenForestGameMode.cpp
[6/21] Compile [Apple] TDDCalendarSubsystem.cpp
[7/21] Compile [Apple] TDDLocationRegistry.cpp
[8/21] Compile [Apple] TDDForbiddenForestLevel.cpp
[9/21] Compile [Apple] TDDOmegaValleyGameMode.cpp
[10/21] Compile [Apple] Module.TDD_GAME.gen.cpp
[11/21] Compile [Apple] TDDAdannaProxyCharacter.cpp
[12/21] Compile [Apple] TDD_GAME.cpp
[13/21] Compile [Apple] TDDPopulationActor.cpp
[14/21] Compile [Apple] TDDWeatherSubsystem.cpp
[15/21] Compile [Apple] TDDOmegaValleyLevel.cpp
[16/21] Compile [Apple] TDDSettlementZone.cpp
[17/21] Compile [Apple] TDDWorldPopulationSubsystem.cpp
[18/21] Link [Apple] TDD_GAME
[19/21] Updating version file: /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Versions.xcconfig [NoUba]
[20/21] ApplePostBuildSync Executing PostBuildSync [/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME] [NoUba]
Discovering modules, targets and source code for project...
Adding projects for all targets...
Adding projects for all targets took 0.18s
Adding projects for all game projects took 0.00s
Adding projects for all modules took 0.41s
/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/MetalShaderConverter.build.cs: warning: Referenced directory '/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/include/metal_irconverter_ext' does not exist.
Compiling with Mac SDK 27.2, minimum Target OS version 14.00
Adding additional Xcode project info took 0.39s
Writing project files...
Writing xcode workspace /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFiles/TDD_GAME_Mac_TDD_GAME.xcworkspace
Writing project files... 100%
Writing project files took 0.11s
params: UBT_NO_POST_DEPLOY=true /Applications/Xcode.app/Contents/Developer/usr/bin/xcodebuild build -workspace "/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFiles/TDD_GAME_Mac_TDD_GAME.xcworkspace" -scheme "TDD_GAME" -configuration "Development" -destination generic/platform="macOS" CODE_SIGN_ALLOW_ENTITLEMENTS_MODIFICATION=YES  -allowProvisioningUpdates UE_XCODE_BUILD_MODE=PostBuildSync -hideShellScriptEnvironment
No certs of truth reported, skipping certificate verification...
Known Apple certificate for this team is installed!
Command line invocation:
    /Applications/Xcode.app/Contents/Developer/usr/bin/xcodebuild build -workspace /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFiles/TDD_GAME_Mac_TDD_GAME.xcworkspace -scheme TDD_GAME -configuration Development -destination generic/platform=macOS CODE_SIGN_ALLOW_ENTITLEMENTS_MODIFICATION=YES -allowProvisioningUpdates UE_XCODE_BUILD_MODE=PostBuildSync -hideShellScriptEnvironment

Build settings from command line:
    CODE_SIGN_ALLOW_ENTITLEMENTS_MODIFICATION = YES
    UE_XCODE_BUILD_MODE = PostBuildSync

2026-11-22 14:44:24.498 xcodebuild[84375:5677292] [MT] IDESchemeActionsInvocationRecord: Device <IDEOSXSupportCore.IDEMacPlaceholder: 0x7c95c1a580 (Any Mac | undefined_arch)> is missing operatingSystemVersion, operatingSystemVersionWithBuildNumber.
Run pre-actions

SchemeAction Touch\ UBT\ generated\ tiles /var/folders/gv/4b3jfs991n9_df6ppdx1lx_h0000gn/T/SchemeScriptAction-hPJhsK.sh
    cd /var/folders/gv/4b3jfs991n9_df6ppdx1lx_h0000gn/T/
    /bin/sh -c /var/folders/gv/4b3jfs991n9_df6ppdx1lx_h0000gn/T/SchemeScriptAction-hPJhsK.sh

ComputePackagePrebuildTargetDependencyGraph

CreateBuildRequest

SendProjectDescription

CreateBuildOperation

ComputeTargetDependencyGraph
note: Building targets in dependency order
note: Target dependency graph (1 target)
    Target 'TDD_GAME' in project 'TDD_GAME (Mac)' (no dependencies)

GatherProvisioningInputs

CreateBuildDescription

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -v -E -dM -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.sdk -x c -c /dev/null

ExecuteExternalTool /Applications/Xcode.app/Contents/Developer/usr/bin/actool --version --output-format xml1

Build description signature: 459aaed6d8f36134945fb12a911b1ad2
Build description path: /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFilesMac/build/XCBuildData/459aaed6d8f36134945fb12a911b1ad2.xcbuilddata
CreateBuildDirectory /Users/mhoodpc/Library/Developer/Xcode/DerivedData/SDKExplicitPrecompiledModules
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFiles
    builtin-create-build-directory /Users/mhoodpc/Library/Developer/Xcode/DerivedData/SDKExplicitPrecompiledModules

CreateBuildDirectory /Users/mhoodpc/Library/Developer/Xcode/DerivedData/CompilationCache.noindex
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFiles
    builtin-create-build-directory /Users/mhoodpc/Library/Developer/Xcode/DerivedData/CompilationCache.noindex

CreateBuildDirectory /Users/mhoodpc/Library/Developer/Xcode/DerivedData/ModuleCache.noindex
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFiles
    builtin-create-build-directory /Users/mhoodpc/Library/Developer/Xcode/DerivedData/ModuleCache.noindex

CreateBuildDirectory /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFiles
    builtin-create-build-directory /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries

CreateBuildDirectory /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/SharedPrecompiledHeaders
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFiles
    builtin-create-build-directory /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/SharedPrecompiledHeaders

CreateBuildDirectory /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/SwiftExplicitPrecompiledModules
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFiles
    builtin-create-build-directory /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/SwiftExplicitPrecompiledModules

CreateBuildDirectory /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFiles
    builtin-create-build-directory /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac

CreateBuildDirectory /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/ExplicitPrecompiledModules
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFiles
    builtin-create-build-directory /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/ExplicitPrecompiledModules

CreateBuildDirectory /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/EagerLinkingTBDs/Mac
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFiles
    builtin-create-build-directory /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/EagerLinkingTBDs/Mac

MkDir /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app (in target 'TDD_GAME' from project 'TDD_GAME (Mac)')
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFilesMac
    /bin/mkdir -p /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app

MkDir /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app/Contents/Resources (in target 'TDD_GAME' from project 'TDD_GAME (Mac)')
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFilesMac
    /bin/mkdir -p /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app/Contents/Resources

MkDir /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app/Contents (in target 'TDD_GAME' from project 'TDD_GAME (Mac)')
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFilesMac
    /bin/mkdir -p /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app/Contents

WriteAuxiliaryFile /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ (Mac).build/Mac/TDD_GAME.build/TDD_GAME.DependencyMetadataFileList (in target 'TDD_GAME' from project 'TDD_GAME (Mac)')
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFilesMac
    write-file /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ \(Mac\).build/Mac/TDD_GAME.build/TDD_GAME.DependencyMetadataFileList

WriteAuxiliaryFile /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ (Mac).build/Mac/TDD_GAME.build/TDD_GAME.DependencyStaticMetadataFileList (in target 'TDD_GAME' from project 'TDD_GAME (Mac)')
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFilesMac
    write-file /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ \(Mac\).build/Mac/TDD_GAME.build/TDD_GAME.DependencyStaticMetadataFileList

WriteAuxiliaryFile /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ (Mac).build/Mac/TDD_GAME.build/Script-A1CA9F53ED4318B2B72D362F.sh (in target 'TDD_GAME' from project 'TDD_GAME (Mac)')
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFilesMac
    write-file /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ \(Mac\).build/Mac/TDD_GAME.build/Script-A1CA9F53ED4318B2B72D362F.sh

WriteAuxiliaryFile /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ (Mac).build/Mac/TDD_GAME.build/DerivedSources/Entitlements.plist (in target 'TDD_GAME' from project 'TDD_GAME (Mac)')
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFilesMac
    write-file /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ \(Mac\).build/Mac/TDD_GAME.build/DerivedSources/Entitlements.plist

ProcessProductPackaging /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Build/Mac/Resources/Sandbox.Server.entitlements /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ (Mac).build/Mac/TDD_GAME.build/TDD_GAME.app-Simulated.xcent (in target 'TDD_GAME' from project 'TDD_GAME (Mac)')
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFilesMac

    Entitlements:

    {
}

    builtin-productPackagingUtility /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Build/Mac/Resources/Sandbox.Server.entitlements -entitlements -format xml -o /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ \(Mac\).build/Mac/TDD_GAME.build/TDD_GAME.app-Simulated.xcent

ProcessProductPackaging /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Build/Mac/Resources/Sandbox.Server.entitlements /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ (Mac).build/Mac/TDD_GAME.build/TDD_GAME.app.xcent (in target 'TDD_GAME' from project 'TDD_GAME (Mac)')
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFilesMac

    Entitlements:

    {
    "com.apple.security.app-sandbox" = 1;
    "com.apple.security.get-task-allow" = 1;
    "com.apple.security.network.client" = 1;
    "com.apple.security.network.server" = 1;
}

    builtin-productPackagingUtility /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Build/Mac/Resources/Sandbox.Server.entitlements -entitlements -format xml -o /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ \(Mac\).build/Mac/TDD_GAME.build/TDD_GAME.app.xcent

ProcessProductPackagingDER /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ (Mac).build/Mac/TDD_GAME.build/TDD_GAME.app-Simulated.xcent /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ (Mac).build/Mac/TDD_GAME.build/TDD_GAME.app-Simulated.xcent.der (in target 'TDD_GAME' from project 'TDD_GAME (Mac)')
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFilesMac
    /usr/bin/derq query -f xml -i /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ \(Mac\).build/Mac/TDD_GAME.build/TDD_GAME.app-Simulated.xcent -o /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ \(Mac\).build/Mac/TDD_GAME.build/TDD_GAME.app-Simulated.xcent.der --raw

ProcessProductPackagingDER /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ (Mac).build/Mac/TDD_GAME.build/TDD_GAME.app.xcent /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ (Mac).build/Mac/TDD_GAME.build/TDD_GAME.app.xcent.der (in target 'TDD_GAME' from project 'TDD_GAME (Mac)')
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFilesMac
    /usr/bin/derq query -f xml -i /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ \(Mac\).build/Mac/TDD_GAME.build/TDD_GAME.app.xcent -o /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ \(Mac\).build/Mac/TDD_GAME.build/TDD_GAME.app.xcent.der --raw

CpResource /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app/Contents/Resources/UEMetadata /Users/Shared/Epic\ Games/UE_5.8/Engine/Build/Mac/Resources/UEMetadata (in target 'TDD_GAME' from project 'TDD_GAME (Mac)')
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFilesMac
    builtin-copy -exclude .DS_Store -exclude CVS -exclude .svn -exclude .git -exclude .hg -strip-unsigned-binaries -strip-deterministic -strip-tool /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/strip -resolve-src-symlinks /Users/Shared/Epic\ Games/UE_5.8/Engine/Build/Mac/Resources/UEMetadata /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app/Contents/Resources

MkDir /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ (Mac).build/Mac/TDD_GAME.build/assetcatalog_output/unthinned (in target 'TDD_GAME' from project 'TDD_GAME (Mac)')
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFilesMac
    /bin/mkdir -p /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ \(Mac\).build/Mac/TDD_GAME.build/assetcatalog_output/unthinned

MkDir /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ (Mac).build/Mac/TDD_GAME.build/assetcatalog_output/thinned (in target 'TDD_GAME' from project 'TDD_GAME (Mac)')
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFilesMac
    /bin/mkdir -p /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ \(Mac\).build/Mac/TDD_GAME.build/assetcatalog_output/thinned

CompileAssetCatalogVariant thinned /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app/Contents/Resources /Users/Shared/Epic\ Games/UE_5.8/Engine/Build/Mac/Resources/Assets.xcassets (in target 'TDD_GAME' from project 'TDD_GAME (Mac)')
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFilesMac
    /Applications/Xcode.app/Contents/Developer/usr/bin/actool /Users/Shared/Epic\ Games/UE_5.8/Engine/Build/Mac/Resources/Assets.xcassets --compile /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ \(Mac\).build/Mac/TDD_GAME.build/assetcatalog_output/thinned --output-format human-readable-text --notices --warnings --export-dependency-info /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ \(Mac\).build/Mac/TDD_GAME.build/assetcatalog_dependencies_thinned --output-partial-info-plist /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ \(Mac\).build/Mac/TDD_GAME.build/assetcatalog_generated_info.plist_thinned --app-icon AppIcon --enable-on-demand-resources NO --development-region English --target-device mac --minimum-deployment-target 14.00 --platform macosx
/* com.apple.actool.compilation-results */
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME (Mac).build/Mac/TDD_GAME.build/assetcatalog_generated_info.plist_thinned
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME (Mac).build/Mac/TDD_GAME.build/assetcatalog_output/thinned/AppIcon.icns
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME (Mac).build/Mac/TDD_GAME.build/assetcatalog_output/thinned/Assets.car


LinkAssetCatalog /Users/Shared/Epic\ Games/UE_5.8/Engine/Build/Mac/Resources/Assets.xcassets (in target 'TDD_GAME' from project 'TDD_GAME (Mac)')
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFilesMac
    builtin-linkAssetCatalog --thinned /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ \(Mac\).build/Mac/TDD_GAME.build/assetcatalog_output/thinned --thinned-dependencies /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ \(Mac\).build/Mac/TDD_GAME.build/assetcatalog_dependencies_thinned --thinned-info-plist-content /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ \(Mac\).build/Mac/TDD_GAME.build/assetcatalog_generated_info.plist_thinned --unthinned /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ \(Mac\).build/Mac/TDD_GAME.build/assetcatalog_output/unthinned --unthinned-dependencies /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ \(Mac\).build/Mac/TDD_GAME.build/assetcatalog_dependencies_unthinned --unthinned-info-plist-content /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ \(Mac\).build/Mac/TDD_GAME.build/assetcatalog_generated_info.plist_unthinned --output /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app/Contents/Resources --plist-output /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ \(Mac\).build/Mac/TDD_GAME.build/assetcatalog_generated_info.plist
note: Emplaced /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app/Contents/Resources/AppIcon.icns (in target 'TDD_GAME' from project 'TDD_GAME (Mac)')
note: Emplaced /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app/Contents/Resources/Assets.car (in target 'TDD_GAME' from project 'TDD_GAME (Mac)')

ProcessInfoPlistFile /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app/Contents/Info.plist /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Build/Mac/Resources/Info.Template.plist (in target 'TDD_GAME' from project 'TDD_GAME (Mac)')
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFilesMac
    builtin-infoPlistUtility /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Build/Mac/Resources/Info.Template.plist -producttype com.apple.product-type.application -genpkginfo /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app/Contents/PkgInfo -expandbuildsettings -format xml -platform macosx -additionalcontentfile /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ \(Mac\).build/Mac/TDD_GAME.build/assetcatalog_generated_info.plist -o /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app/Contents/Info.plist

PhaseScriptExecution Copy\ Executable\ and\ Staged\ Data\ into\ .app /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ (Mac).build/Mac/TDD_GAME.build/Script-A1CA9F53ED4318B2B72D362F.sh (in target 'TDD_GAME' from project 'TDD_GAME (Mac)')
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFilesMac
    /bin/sh -c /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\\\ \\\(Mac\\\).build/Mac/TDD_GAME.build/Script-A1CA9F53ED4318B2B72D362F.sh
Copying executable and any standalone dylibs into /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app/Contents/MacOS but do not overwrite unless src is newer
=========================================================================================
WARNING: To run, you must have a valid staged build directory. The Staged location is:
  /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Saved/StagedBuilds/Mac
Use the editor's Platforms menu, or run a command like::
./RunUAT.sh BuildCookRun -platform=Mac -project=<project> -build -cook -stage -pak
=========================================================================================

CodeSign /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app (in target 'TDD_GAME' from project 'TDD_GAME (Mac)')
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFilesMac

    Signing Identity:     "Sign to Run Locally"

    /usr/bin/codesign --force --sign - --entitlements /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/TDD_GAME\ \(Mac\).build/Mac/TDD_GAME.build/TDD_GAME.app.xcent --timestamp\=none --generate-entitlement-der --strip-disallowed-xattrs /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app: replacing existing signature

RegisterExecutionPolicyException /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app (in target 'TDD_GAME' from project 'TDD_GAME (Mac)')
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFilesMac
    builtin-RegisterExecutionPolicyException /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app

Validate /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app (in target 'TDD_GAME' from project 'TDD_GAME (Mac)')
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFilesMac
    builtin-validationUtility /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app -no-validate-extension -infoplist-subpath Contents/Info.plist

Touch /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app (in target 'TDD_GAME' from project 'TDD_GAME (Mac)')
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFilesMac
    /usr/bin/touch -c /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app

RegisterWithLaunchServices /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app (in target 'TDD_GAME' from project 'TDD_GAME (Mac)')
    cd /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFilesMac
    builtin-lsregisterurl --record-path /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/ProjectFilesMac/build/XCBuildData/registered-launchservices.txt -- /System/Library/Frameworks/CoreServices.framework/Versions/Current/Frameworks/LaunchServices.framework/Versions/Current/Support/lsregister -f -R -trusted /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME.app

PruneExplicitPrecompiledModules /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/SwiftExplicitPrecompiledModules

PruneExplicitPrecompiledModules /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/ExplicitPrecompiledModules

PruneExplicitPrecompiledModules /Users/mhoodpc/Library/Developer/Xcode/DerivedData/SDKExplicitPrecompiledModules

** BUILD SUCCEEDED **

[21/21] WriteMetadata TDD_GAME.target [NoUba]

Total time in Unreal Build Accelerator local executor: 35.34 seconds
Output binary: /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Binaries/Mac/TDD_GAME
Deploying TDD_GAME Mac Development...
Deploying now!

Result: Succeeded
Total execution time: 37.13 seconds
Trace written to file /Users/mhoodpc/Library/Application Support/Epic/UnrealBuildTool/Trace.uba with size 9.9kb
@@TDD_BUILD_OUTPUT_END@@
[diag] PASS  SUCCESS — Build.sh exited 0: TDD_GAME COMPILED (compile-verified ONLY, not runtime).
[diag] NEXT (owner): open TDD_GAME.uproject in the UE 5.8 editor, create
        OMEGA_VALLEY_PHASE1.umap (empty level), set World Settings -> Game Mode
        = TDD_GAME.TDDOmegaValleyGameMode, place a Player Start, PIE.
[diag] See docs/06_IMPLEMENTATION/WORLD/PHASE1_IMPLEMENTATION_EVIDENCE_AND_BUILD_PROCEDURE.md §4.4-4.5.
mhoodpc TDD% 