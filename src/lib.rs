use eframe::egui;

#[derive(Default)]
pub struct MyApp {
    icon: Option<egui::TextureHandle>,
}

fn load_image(cc: &eframe::CreationContext<'_>, bytes: &[u8], name: &str) -> Option<egui::TextureHandle> {
    if let Ok(img) = image::load_from_memory(bytes) {
        let size = [img.width() as usize, img.height() as usize];
        let rgba = img.to_rgba8();
        let color_image = egui::ColorImage::from_rgba_unmultiplied(size, rgba.as_flat_samples().as_slice());
        return Some(cc.egui_ctx.load_texture(name, color_image, Default::default()));
    }
    None
}

impl MyApp {
    pub fn new(cc: &eframe::CreationContext<'_>) -> Self {
        Self {
            icon: load_image(cc, include_bytes!("../assets/icon.png"), "icon"),
        }
    }
}

impl eframe::App for MyApp {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        egui::CentralPanel::default().show(ctx, |ui| {
            // Upar status bar se takrane ka fix
            ui.add_space(40.0);
            ui.heading("AT World Matter");
            ui.add_space(20.0);

            if let Some(tex) = &self.icon {
                // Photo ko center me aur chhota karke dikhao
                let size = tex.size_vec2();
                let max_w = 250.0;
                let scale = max_w / size.x;
                let show_size = egui::vec2(max_w, size.y * scale);
                ui.horizontal(|ui| {
                    ui.add_space((ui.available_width() - show_size.x) / 2.0);
                    ui.image((tex.id(), show_size));
                });
            } else {
                ui.label("Welcome to AT World Matter App");
                ui.label("Icon load nahi hua - icon.png check karo");
            }
        });
    }
}

#[cfg(target_os = "android")]
#[no_mangle]
pub fn android_main(app: android_activity::AndroidApp) {
    let options = eframe::NativeOptions {
        android_app: Some(app),
        ..Default::default()
    };
    let _ = eframe::run_native(
        "AT World Matter",
        options,
        Box::new(|cc| Ok(Box::new(MyApp::new(cc)))),
    );
}
