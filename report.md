# API Reliability Monitor — SLA Report

> Last updated: **2026-05-23 06:46 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 69.35% | 3251.4 | 10206.7 | 1000ms | 266/868 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 129.7 | 4595.4 | 1500ms | 4/868 |
| ❌ | `nasa_apod` | 78.0% | 58.29% | 2868.2 | 10549.1 | 2000ms | 362/868 |
| ❌ | `ipapi_check` | 80.53% | 100.0% | 153.9 | 431.8 | 2500ms | 0/868 |
| ⚠️ | `rest_countries` | 98.73% | 98.27% | 346.9 | 10221.5 | 2500ms | 15/868 |
| ⚠️ | `open_meteo_weather` | 98.96% | 97.12% | 700.1 | 14877.1 | 2000ms | 25/868 |
| ✅ | `dog_ceo_random` | 99.42% | 95.16% | 618.9 | 10244.1 | 2500ms | 42/868 |
| ✅ | `catfact_random` | 99.65% | 99.19% | 269.0 | 10080.2 | 3000ms | 7/868 |
| ✅ | `coingecko_bitcoin` | 99.65% | 100.0% | 97.8 | 253.3 | 1500ms | 0/868 |
| ✅ | `useless_fact` | 99.77% | 99.54% | 613.8 | 10229.6 | 2500ms | 4/868 |
| ✅ | `agify_name` | 99.88% | 99.65% | 389.3 | 16112.2 | 2000ms | 3/868 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.77% | 230.3 | 3882.8 | 2000ms | 2/868 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4729.0 | 77.78% |
| `numbers_trivia` | 03:00 | 4635.3 | 44.44% |
| `numbers_trivia` | 07:00 | 3915.1 | 37.04% |
| `nasa_apod` | 17:00 | 3847.1 | 48.98% |
| `numbers_trivia` | 12:00 | 3843.8 | 36.11% |
| `numbers_trivia` | 05:00 | 3808.4 | 36.0% |
| `nasa_apod` | 11:00 | 3767.9 | 46.0% |
| `numbers_trivia` | 10:00 | 3747.3 | 35.29% |
| `numbers_trivia` | 14:00 | 3674.8 | 36.36% |
| `nasa_apod` | 05:00 | 3555.0 | 60.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
