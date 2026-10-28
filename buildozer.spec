      - name: Build APK
        run: |
          rm -rf .buildozer bin
          mkdir -p ~/.android/licenses
          echo "8933bad161af4178b1185d1a37fbf41ea5269c55" > ~/.android/licenses/android-sdk-license
          echo "d56f5187479451eabf01fb78af6dfcb131a6481e" >> ~/.android/licenses/android-sdk-license
          echo "24333f8a63b6825ea9c5514f83c1059b8ea04e4f" >> ~/.android/licenses/android-sdk-license
          echo "8933bad161af4178b1185d1a37fbf41ea5269c55" > ~/.android/licenses/android-sdk-preview-license
          cat ~/.android/licenses/android-sdk-license
          python3 -m buildozer -v android debug
