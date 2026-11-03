name: build
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: 17
      - uses: nttld/setup-ndk@v1
        id: ndk
        with:
          ndk-version: r26b
      - run: |
          echo y | $ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager --install "platforms;android-33" "build-tools;33.0.2" "platform-tools"
      - uses: dtolnay/rust-toolchain@stable
        with:
          targets: aarch64-linux-android
      - run: cargo install cargo-apk
      - name: Build APK
        env:
          ANDROID_HOME: /usr/local/lib/android/sdk
          ANDROID_NDK_ROOT: ${{ steps.ndk.outputs.ndk-path }}
        run: |
          unset ANDROID_SDK_ROOT
          keytool -genkey -v -keystore debug.keystore -alias androiddebugkey -keyalg RSA -keysize 2048 -validity 10000 -storepass android -keypass android -dname "CN=Android,O=Android,C=US"
          cargo apk build --release
      - uses: actions/upload-artifact@v4
        with:
          name: AT-APK
          path: target/**/*.apk
