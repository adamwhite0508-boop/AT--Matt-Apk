use eframe::egui;

#[derive(Default)]
pub struct MyApp {
    header: Option<egui::TextureHandle>,
    icon: Option<egui::TextureHandle>,
    banner: Option<egui::TextureHandle>,
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
            header: load_image(cc, include_bytes!("../assets/main_header.png"), "header"),
            icon: load_image(cc, include_bytes!("../assets/icon.png"), "icon"),
            banner: load_image(cc, include_bytes!("../assets/login_banner.png"), "banner"),
        }
    }
}

impl eframe::App for MyApp {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        egui::CentralPanel::default().show(ctx, |ui| {
            ui.heading("AT World Matter");

            if let Some(tex) = &self.banner {
                ui.image(tex);
            }
            ui.add_space(10.0);
            if let Some(tex) = &self.header {
                ui.image(tex);
            }
            ui.add_space(10.0);
            if let Some(tex) = &self.icon {
                ui.image(tex);
            }
        });
    }
}

// Ye wala part Android ke liye sabse zaroori hai - isi se crash fix hoga
#[cfg(target_os = "android")]
#[no_mangle]
pub fn android_main(app: winit::platform::android::activity::AndroidApp) {
    use winit::platform::android::EventLoopBuilderExtAndroid;
    android_logger::init_once(
        android_logger::Config::default().with_max_level(log::LevelFilter::Info),
    );
    let event_loop = winit::event_loop::EventLoopBuilder::new()
        .with_android_app(app)
        .build()
        .expect("Failed to build event loop");

    let mut app_creator = |cc: &eframe::CreationContext<'_>| {
        Ok(Box::new(MyApp::new(cc)) as Box<dyn eframe::App>)
    };

    let _ = eframe::run_native(
        "AT World Matter",
        eframe::NativeOptions::default(),
        Box::new(|cc| Ok(Box::new(MyApp::new(cc)))),
    );
}
