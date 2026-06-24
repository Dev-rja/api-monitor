# API Reliability Monitor — SLA Report

> Last updated: **2026-06-24 11:30 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 77.38% | 2456.1 | 10206.7 | 1000ms | 266/1176 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 125.0 | 4595.4 | 1500ms | 4/1176 |
| ❌ | `nasa_apod` | 74.49% | 51.11% | 3306.1 | 11152.5 | 2000ms | 575/1176 |
| ❌ | `ipapi_check` | 76.53% | 99.91% | 155.7 | 4507.0 | 2500ms | 1/1176 |
| ⚠️ | `rest_countries` | 98.72% | 98.38% | 335.9 | 10221.5 | 2500ms | 19/1176 |
| ⚠️ | `open_meteo_weather` | 98.98% | 96.94% | 711.7 | 14877.1 | 2000ms | 36/1176 |
| ✅ | `useless_fact` | 99.57% | 99.66% | 631.8 | 10229.6 | 2500ms | 4/1176 |
| ✅ | `dog_ceo_random` | 99.57% | 96.43% | 548.7 | 10244.1 | 2500ms | 42/1176 |
| ✅ | `catfact_random` | 99.74% | 99.23% | 261.4 | 10080.2 | 3000ms | 9/1176 |
| ✅ | `coingecko_bitcoin` | 99.74% | 100.0% | 95.8 | 253.3 | 1500ms | 0/1176 |
| ✅ | `agify_name` | 99.91% | 99.74% | 376.3 | 16112.2 | 2000ms | 3/1176 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.83% | 217.8 | 3882.8 | 2000ms | 2/1176 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4721.6 | 69.7% |
| `nasa_apod` | 17:00 | 4293.2 | 56.25% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 09:00 | 4114.4 | 54.0% |
| `nasa_apod` | 01:00 | 4107.5 | 60.0% |
| `nasa_apod` | 11:00 | 3739.0 | 52.31% |
| `nasa_apod` | 18:00 | 3605.5 | 52.54% |
| `nasa_apod` | 20:00 | 3451.4 | 48.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
